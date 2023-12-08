import { ArrowRightIcon } from "@heroicons/react/20/solid"

export type Todo = {
  id: number
  user: {
    username: string
  }
  title: string
  description: string
  completed: boolean
  priority: string
  url: string
  created_at: string
  updated_at: string
}

export default function TodoItem({ todo }: { todo: Todo }) {
  return (
    <div
      className={`w-full shadow-sm rounded-md p-4 space-y-2 ${
        todo.priority == "High"
          ? "border-r-4 border-r-teal-400"
          : "border-r-4 border-r-blue-400"
      }`}
    >
      <p className="title text-xl">{todo.title}</p>
      <p className="description text-sm line-clamp-1 text-gray-500">
        {todo.description}
      </p>
      <div className="flex item-center justify-between mt-2">
        <p
          className={`status ${
            todo.completed ? "text-[#1a73e8]" : "text-red-500"
          }`}
        >
          {todo.completed ? "Completed" : "Pending"}
        </p>
        <a href={`/edit/${todo.id}`} className=" hover:cursor-pointer">
          <p className="edit">
            <ArrowRightIcon className="text-slate-700 h-5 w-5" />
          </p>
        </a>
      </div>
    </div>
  )
}
