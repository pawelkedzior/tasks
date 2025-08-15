<script setup lang="ts">
    const title = ref("Powitanie")
    const msg = ref("Cześć świecie")
</script>

<template>
    <UCard class="m-8">
        <UAlert class="w-64 mx-auto" :title="title" :description="msg"/>
    </UCard>
</template>
