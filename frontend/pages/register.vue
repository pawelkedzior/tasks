<script setup lang="ts">
    definePageMeta({
        middleware: "guest"
    })
    const {$api} = useNuxtApp()
    const toast = useToast()

    function register(loginData: {username: string, password: string}) {
        $api("/auth/register", {
            method: "PUT",
            body: loginData
        }).then((_response) => {
            toast.add({title: "Rejestracja udana", description: "Rejestracja przebiegła pomyślnie. Teraz się zaloguj.", color: "success"})
            navigateTo("/login")
        }).catch((_error) => {
            toast.add({title: "Błąd rejestracji", description: "Rejestracja nieudana. Klient o takim loginie już istnieje", color: "error"})
        })
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
