import axios from "axios"
import { useNavigate } from "react-router-dom"

export default function Register() {
  const navigate = useNavigate()

  const register = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const username = formData.get("username")
    const email = formData.get("email")
    const password = formData.get("password")
    const url = "http://localhost:8000/accounts/register/"

    axios
      .post(url, { username: username, email: email, password: password })
      .then(() => navigate("/login"))
      .catch((err) => {
        console.log(err.response.data.error)
      })
  }

  return (
    <div className="lg:hidden">
      <div className="flex h-[100dvh] flex-col items-center justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Create account
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" onSubmit={register} method="POST">
            <div>
              <label
                htmlFor="username"
                className="block text-lg font-medium leading-6 text-gray-900"
              >
                Username
              </label>
              <div className="mt-2">
                <input
                  id="username"
                  name="username"
                  type="text"
                  className="block w-full rounded-md border-[1px] py-2 px-3 outline-none text-gray-900"
                />
              </div>
            </div>

            <div>
              <label
                htmlFor="email"
                className="block text-lg font-medium leading-6 text-gray-900"
              >
                Email
              </label>
              <div className="mt-2">
                <input
                  id="email"
                  name="email"
                  type="email"
                  className="block w-full rounded-md border-[1px] py-2 px-3 outline-none text-gray-900"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label
                  htmlFor="password"
                  className="block text-lg font-medium leading-6 text-gray-900"
                >
                  Password
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  className="block w-full rounded-md border-[1px] py-2 px-3 outline-none text-gray-900"
                />
              </div>
            </div>

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-2 text-lg font-semibold text-white shadow-sm"
              >
                Submit
              </button>
            </div>
            <div className="not-member flex items-center space-x-2">
              <p>Already have an account</p>{" "}
              <a href="/login" className="underline text-blue-500">
                login
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}
