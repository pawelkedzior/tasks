<script setup lang="ts">
    import type {CommandPaletteItem} from "#ui/components/CommandPalette.vue"

    const tasksOps = useTasks()

    const groups = computed(() => (
        [{
            id: "tasks",
            label: "Zadania",
            items: tasksOps.tasks.value?.map((task: Task) => ({label: task.name, onSelect: () => task.is_done = !task.is_done}))
        }]
    ))

    const tasksDone = computed(() => (
        tasksOps.tasks.value?.filter((task: Task) => task.is_done).map((task: Task) => ({label: task.name}))
    ))

    const newTaskName: Ref<string> = ref("")

    const alreadyExists = computed(() => !!tasksOps.tasks.value?.find((task: Task) => task.name === newTaskName.value))

    const addTask = () => {
        tasksOps.addTask({name: newTaskName.value, is_done: false})
        newTaskName.value = ""
    }

    const removeTask = (event: Event, item: CommandPaletteItem) => {
        event.stopPropagation()
        const taskToRemove = tasksOps.tasks.value?.find((task) => task.name === item.label)
        if (taskToRemove)
            tasksOps.removeTask(taskToRemove)
    }

    watch(tasksDone, (newValue, oldValue) => {
        if (!newValue || !oldValue || newValue.length === oldValue.length)
            return
        const updatedTaskLabel = new Set(newValue.map((task) => task.label))
            .symmetricDifference(new Set(oldValue.map((task) => task.label))).values().next().value
        if (!updatedTaskLabel)
            return
        const updatedTask = tasksOps.tasks.value?.find((task) => task.name === updatedTaskLabel)
        if (updatedTask)
            tasksOps.updateTask(updatedTask)
    })
</script>

<template>
    <UCommandPalette :model-value="tasksDone" multiple :groups="groups" :placeholder="'Wyszukaj zadanie...'">
        <template #item-leading="{item}">
            <UButton icon="i-lucide-trash" color="neutral" size="xs" @click="(event: Event) => removeTask(event, item)"/>
        </template>
        <template #footer>
            <div class="grid grid-cols-8 mt-2">
                <UBadge color="neutral" variant="soft" label="Nazwa zadania" class="mr-2"/>
                <UInput v-model="newTaskName" size="xs" class="col-span-2"/>
                <UTooltip :text="alreadyExists ? 'Takie zadanie już istnieje' : ''">
                    <UButton
                        label="Dodaj zadanie"
                        size="xs"
                        :disabled="!newTaskName || alreadyExists"
                        class="col-start-8"
                        @click="addTask"
                    />
                </UTooltip>
            </div>
        </template>
    </UCommandPalette>
</template>
