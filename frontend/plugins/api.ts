export default defineNuxtPlugin((nuxtApp) => {
    const {auth: token} = useAuth()
    const config = useRuntimeConfig()

    const api = $fetch.create({
        baseURL: config.public.backendURL as string,
        onRequest({request, options, error}) {
            if (token.value) {
                options.headers.set("Authorization", `Bearer ${token.value}`)
            }
        },
        async onResponseError({response}) {
            if (response.status === 401) {
                token.value = ""
                await nuxtApp.runWithContext(() => navigateTo("/login"))
            }
        }
    })

    return {
        provide: {
            api
        }
    }
})
