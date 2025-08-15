<script setup lang="ts">
    const loginData = reactive({
        login: "",
        password: ""
    })

    const logIn = () => {

    }
</script>

<template>
    <div class="flex items-center">
        <UCard variant="subtle" class="w-120 mx-auto">
            <UForm :state="loginData" @submit="logIn" class="w-64 mx-auto grid grid-cols-1 items-center">
                <UFormField label="Login" name="login">
                    <UInput v-model="loginData.login" class="w-full"/>
                </UFormField>
                <UFormField label="Hasło" name="password">
                    <UInput v-model="loginData.password" type="password" class="w-full"/>
                </UFormField>
                <UButton label="Zaloguj się" type="submit" class="justify-center my-2"/>
                <USeparator label="Nie masz konta?" class="my-2"/>
                <UButton label="Zarejestruj się" class="justify-center" color="neutral" variant="ghost"/>
            </UForm>
        </UCard>
    </div>
</template>

<style scoped>

</style>
