<script setup lang="ts">
    definePageMeta({
        middleware: "auth"
    })
</script>

<template>
    <div class="p-4">
        <UCard>
            <TaskCounter/>
            <USeparator class="mt-8"/>
            <ClientOnly>
                <TaskList class="mt-2"/>
                <template #fallback>
                    <USkeleton class="mt-4 h-8 w-full"/>
                    <USkeleton class="mt-4 h-32 w-full"/>
                    <USkeleton class="mt-4 h-8 w-full"/>
                </template>
            </ClientOnly>
        </UCard>
    </div>
</template>
