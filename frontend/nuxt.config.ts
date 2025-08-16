//https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: ["@nuxt/ui", "@nuxt/eslint"],
    devtools: {enabled: true},
    css: ["~/assets/css/main.css"],
    runtimeConfig: {
        public: {
            backendURL: "http://localhost:8000/"
        }
    },
    compatibilityDate: "2025-07-15",
    eslint: {
        config: {
            stylistic: true
        }
    }
})
