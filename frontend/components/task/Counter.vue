<script setup lang="ts">
    const {tasks} = useTasks()
    const completedTasks = computed(() => tasks.value?.filter((t: Task) => t.is_done).length)
    const totalTasks = computed(() => tasks.value?.length)
</script>

<template>
    <UFormField title="Ukończone zadania" :description="'Ukończono ' + completedTasks + ' z ' + totalTasks + ' zadań'" class="max-w-80">
        <USlider :min="0" :max="totalTasks" :default-value="completedTasks" :disabled="true"/>
    </UFormField>
</template>
