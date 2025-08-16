<script setup lang="ts">
    const props = withDefaults(defineProps<{
        onSubmit: () => void
        register?: boolean
    }>(), {
        register: false
    })

    const loginData = reactive({
        login: "",
        password: ""
    })
</script>

<template>
    <UForm :state="loginData" class="w-64 mx-auto grid grid-cols-1 items-center" @submit="props.onSubmit()">
        <UFormField label="Login" name="login">
            <UInput v-model="loginData.login" class="w-full"/>
        </UFormField>
        <UFormField label="Hasło" name="password">
            <UInput v-model="loginData.password" type="password" class="w-full"/>
        </UFormField>
        <UButton :label="props.register ? 'Zarejestruj się' : 'Zaloguj się'" type="submit" class="justify-center my-2"/>
        <USeparator v-if="!props.register" label="Nie masz konta?" class="my-2"/>
        <UButton v-if="!props.register" to="/register" label="Zarejestruj się" class="justify-center" color="neutral" variant="ghost"/>
    </UForm>
</template>
