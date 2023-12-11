import axios from "axios"
import { useNavigate } from "react-router-dom"

export default function Login() {
  const navigate = useNavigate()

  const login = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const email = formData.get("email")
    const password = formData.get("password")
    const url = "http://localhost:8000/accounts/login/"

    axios
      .post(url, { email: email, password: password })
      .then((res) => res.data)
      .then((data) => {
        const access = data["access"]
        const refresh = data["refresh"]
        localStorage.setItem("access", access)
        localStorage.setItem("refresh", refresh)
        navigate("/")
      })
      .catch((err) => {
        console.log(err.message)
      })
  }

  return (
    <div className="lg:hidden">
      <div className="flex h-[100dvh] flex-col items-center justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Login
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" onSubmit={login} method="POST">
            <div>
              <label
                htmlFor="username"
                className="block text-lg font-medium leading-6 text-gray-900"
              >
                Email Address
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
                Sign in
              </button>
            </div>

            <div className="not-member flex items-center space-x-2">
              <p>Don't have an account</p>{" "}
              <a href="/register" className="underline text-blue-500">
                Register
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}
