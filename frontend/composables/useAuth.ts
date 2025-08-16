export default function() {
    const {$api} = useNuxtApp()
    const toast = useToast()
    const token = useState("authToken", (): Ref<string> => ref(""))
    const isAuthenticated = computed<boolean>(() => token.value !== "")

    async function logIn(loginData: {username: string, password: string}) {
        const acquiredToken = await $api<string>("/auth/login", {
            method: "POST",
            body: loginData
        })

        if (!token) {
            toast.add({title: "Błąd logowania", color: "error"})
            return
        }

        token.value = acquiredToken
        navigateTo("/")
    }

    return {isAuthenticated, logIn, token}
}
