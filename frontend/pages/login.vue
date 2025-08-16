<script setup lang="ts">
    function logIn() {

    }
</script>

<template>
    <div class="flex items-center">
        <UCard variant="subtle" class="w-120 mx-auto">
            <template #header>
                <UAlert title="Formularz logowania" variant="outline"/>
            </template>
            <AuthenticationForm @submit="logIn"/>
        </UCard>
    </div>
</template>
