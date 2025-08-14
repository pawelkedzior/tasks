// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: ['@nuxt/ui', '@nuxt/eslint'],
    css: ['~/assets/css/main.css'],
    compatibilityDate: '2025-07-15',
    eslint: {
        config: {
          stylistic: true
        }
    }
    devtools: { enabled: true }
})
