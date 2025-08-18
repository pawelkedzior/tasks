export default function() {
    const {$api} = useNuxtApp()
    const toast = useToast()
    const token = useState(() => useCookie("Session").value || "")
    const isAuthenticated = computed<boolean>(() => token.value != "")

    async function logIn(loginData: {username: string, password: string}) {
        const acquiredToken = await $api<string>("/auth/login", {
            method: "POST",
            body: loginData
        })

        if (!acquiredToken) {
            toast.add({title: "Błąd logowania", color: "error"})
            return
        }

        token.value = acquiredToken
        useCookie("Session").value = acquiredToken

        navigateTo("/")
    }

    return {isAuthenticated, logIn, token}
}
