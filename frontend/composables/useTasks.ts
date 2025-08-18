export interface Task {
    task_id?: string
    is_done: boolean
    name: string
}

export default function() {
    const $api = useNuxtApp().$api
    const {data: tasks, refresh} = useAPI<Task[]>("tasks", {method: "GET"})

    const addTask = async (task: Task) => {
        await $api("tasks", {method: "PUT", body: task})
        await refresh()
    }

    const removeTask = async (task: Task) => {
        await $api("tasks", {method: "DELETE", body: task})
        await refresh()
    }

    const updateTask = async (task: Task) => {
        await $api("tasks", {method: "POST", body: task}).then(async () => {
            await refresh()
        })
    }

    return {tasks, addTask, removeTask, updateTask}
}
