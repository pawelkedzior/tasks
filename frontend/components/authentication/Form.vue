<script setup lang="ts">
    import {object, string} from "yup"

    const props = withDefaults(defineProps<{
        onSubmit: () => void
        register?: boolean
    }>(), {
        register: false
    })

    const schema = object({
        login: string()
            .min(3, "Za krótki login")
            .required("To pole jest wymagane"),
        password: string()
            .min(8, "Hasło musi zawierać przynajmniej 8 znaków")
            .required("To pole jest wymagane")
    })

    const loginData = reactive({
        login: "",
        password: ""
    })
</script>

<template>
    <UForm :state="loginData" :schema="schema" class="w-64 mx-auto grid grid-cols-1 items-center" @submit="props.onSubmit()">
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
