export default function() {
    const {$api} = useNuxtApp()
    const toast = useToast()
    const auth = useCookie("Session")
    const isAuthenticated = computed<boolean>(() => auth.value !== "")

    async function logIn(loginData: {username: string, password: string}) {
        const acquiredToken = await $api<string>("/auth/login", {
            method: "POST",
            body: loginData
        })

        if (!acquiredToken) {
            toast.add({title: "Błąd logowania", color: "error"})
            return
        }

        auth.value = acquiredToken

        navigateTo("/")
    }

    return {isAuthenticated, logIn, auth}
}
