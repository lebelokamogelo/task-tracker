import axios from "axios"
import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import TodoItem, { Todo } from "../components/TodoItem"

export default function HomePage() {
  const navigate = useNavigate()
  const [task, setTask] = useState([])
  const [query, setQuery] = useState("")

  useEffect(() => {
    getTask()
  }, [query])

  const getTask = () => {
    const url = `http://localhost:8000/api/todos/?query=${query}`
    const access = localStorage.getItem("access")

    const headers = {
      "Content-Type": "application/json",
      Authorization: "Bearer " + access,
    }

    axios({
      method: "get",
      url: url,
      headers: headers,
    })
      .then((response) => {
        if (!response.data) {
          throw new Error(`HTTP error! Status: ${response.status}`)
        }
        return response.data
      })
      .then((data) => {
        setTask(data)
        console.log(data)
      })
      .catch((error) => {
        console.error("Fetch error:", error)
      })
  }

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const query = formData.get("query") || ""
    setQuery(query.toString())
    getTask()
    navigate(`/?query=${query}`)
  }

  const logout = () => {
    const url = "http://localhost:8000/accounts/logout/"
    const access = localStorage.getItem("access")

    const headers = {
      "Content-Type": "application/json",
      Authorization: "Bearer " + access,
    }

     const data = {
      refresh_token: localStorage.getItem("refresh")
    }

    axios({
      method: "post",
      url: url,
      headers: headers,
      data: data
    })
      .then(() => {
        localStorage.removeItem("access")
        localStorage.removeItem("refresh")
        navigate("/login")
      })
      .catch((error) => {
        console.error("Logout failed:", error)
      })
  }

  return (
    <div className="px-4 py-2 h-[100dvh] relative lg:hidden">
      <div className="header flex items-center justify-between">
        <a href="/" className="text-xl">
          Tasks
        </a>
        <button className="underline text-lg text-blue-500" onClick={logout}>
          Sign out
        </button>
      </div>

      <div className="search py-4">
        <form method="get" onSubmit={handleSubmit}>
          <input
            type="text"
            name="query"
            placeholder="Search by title and description"
            className="w-full py-2 px-4 outline-none border-2 rounded-md"
          />
        </form>
      </div>

      <div className="todos py-2 space-y-3">
        {task.map((todo: Todo) => (
          <TodoItem todo={todo} key={todo.id} />
        ))}
      </div>
      <a href="/create">
        <div className="create hover:cursor-pointer absolute bottom-4 right-4 py-1 px-3 w-12 h-12 flex items-center justify-center bg-blue-500 text-3xl text-white rounded-full">
          <span>+</span>
        </div>
      </a>
    </div>
  )
}
