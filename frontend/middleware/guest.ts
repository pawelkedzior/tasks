export default defineNuxtRouteMiddleware((_to, _from) => {
    const auth = useAuth() //Or any other auth technique

    if (auth.isAuthenticated.value) {
        return navigateTo("/")
    }
})
