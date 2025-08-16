<script setup lang="ts">
    function register() {

    }
</script>

<template>
    <div class="flex items-center">
        <UCard variant="subtle" class="w-120 mx-auto">
            <template #header>
                <UAlert title="Formularz rejestracji" variant="outline"/>
            </template>
            <AuthenticationForm :register="true" @submit="register"/>
        </UCard>
    </div>
</template>
