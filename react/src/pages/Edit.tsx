import { ArrowLeftIcon } from "@heroicons/react/20/solid"
import axios from "axios"
import { useEffect, useState } from "react"
import { useNavigate, useParams } from "react-router-dom"

export default function Edit() {
  const { id } = useParams()
  const [task, setTask] = useState({
    title: "",
    description: "",
    completed: false,
    priority: "",
  })
  const navigate = useNavigate()

  useEffect(() => {
    getTask()
  }, [id])

  const getTask = () => {
    const url = `http://localhost:8000/api/todo/${id}/`
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
        const title = data["title"]
        const description = data["description"]
        const completed = data["completed"]
        const priority = data["priority"]

        setTask({
          title: title,
          description: description,
          completed: completed,
          priority: priority,
        })
      })
      .catch((error) => {
        console.error("Fetch error:", error)
      })
  }

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const url = `http://localhost:8000/api/todo/${id}/`
    const access = localStorage.getItem("access")

    const headers = {
      "Content-Type": "application/json",
      Authorization: "Bearer " + access,
    }

    const data = {
      title: task?.title,
      description: task?.description,
      completed: task?.completed,
      priority: task?.priority,
    }

    axios({
      method: "put",
      url: url,
      headers: headers,
      data: JSON.stringify(data),
    })
      .then(() => {
        navigate("/")
      })
      .catch((error) => {
        console.error(error)
      })
  }

  return (
    <div className="lg:hidden">
      <div className="header flex items-center px-4 py-2 text-xl">
        <a href="/">
          <ArrowLeftIcon className="text-slate-700 h-7 w-7" />
        </a>
        <p className="w-full text-center">Edit Task</p>
      </div>
      <form
        className="space-y-4 px-4 mt-8"
        onSubmit={handleSubmit}
        method="POST"
      >
        <div>
          <label
            htmlFor="username"
            className="block text-lg font-medium leading-6 text-gray-900"
          >
            Title
          </label>
          <div className="mt-2">
            <input
              name="title"
              type="text"
              value={task?.title}
              onChange={(e) =>
                setTask((todo) => ({ ...todo, title: e.target.value }))
              }
              className="block w-full rounded-md border-[1px] py-2 px-3 outline-none text-gray-900"
            />
          </div>
        </div>
        <div>
          <label
            htmlFor="username"
            className="block text-lg font-medium leading-6 text-gray-900"
          >
            Description
          </label>
          <div className="mt-2">
            <textarea
              name="description"
              value={task?.description}
              onChange={(e) =>
                setTask((todo) => ({ ...todo, description: e.target.value }))
              }
              className="block w-full rounded-md border-[1px] py-2 px-3 h-40 resize-none outline-none text-gray-900"
            />
          </div>
        </div>
        <div>
          <label
            htmlFor="username"
            className="block text-lg font-medium leading-6 text-gray-900"
          >
            Completed
          </label>
          <div className="mt-2">
            <input
              name="completed"
              type="checkbox"
              checked={task?.completed}
              onChange={(e) =>
                setTask((todo) => ({ ...todo, completed: e.target.checked }))
              }
              className="block rounded-md border-[1px] py-2 px-3 outline-none text-gray-900"
            />
          </div>
        </div>

        <div className="flex flex-col">
          <label htmlFor="priority">Select Priority:</label>
          <select
            id="priority"
            name="priority"
            value={task?.priority}
            onChange={(e) =>
              setTask((todo) => ({ ...todo, priority: e.target.value }))
            }
            className="mt-2 w-full rounded-md border-[1px] py-2 px-3 outline-none bg-transparent"
          >
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>

        <div className="mt-4">
          <button
            type="submit"
            className="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-2 text-lg font-semibold text-white shadow-sm"
          >
            Update
          </button>
        </div>
      </form>
    </div>
  )
}
