// @ts-check
import vueEslintParser from "vue-eslint-parser";
import stylistic from "@stylistic/eslint-plugin";
import globals from "globals";
import withNuxt from './.nuxt/eslint.config.mjs'

export default withNuxt(
    {
        plugins: {
            "@stylistic": stylistic
        },
        languageOptions: {
            globals: {
                ...globals.browser,
                ...globals.node
            },

            parser: vueEslintParser,
            ecmaVersion: "latest",
            sourceType: "module",

            parserOptions: {
                project: "./tsconfig.json",
                parser: "@typescript-eslint/parser",

                vueFeatures: {
                    interpolationAsNonHTML: true
                },

                tsconfigRootDir: ".",
                extraFileExtensions: ["vue"]
            }
        },
        rules: {
            "vue/multi-word-component-names": [
                "error",
                {
                    ignores: ["default", "index"]
                }
            ],
            "vue/html-indent": ["error", 4],
            "vue/script-indent": ["error", 4, {baseIndent: 1}],
            "vue/max-attributes-per-line": "off",
            "vue/object-curly-spacing": ["error", "never"],
            "vue/comma-dangle": ["error", "never"],
            "vue/html-closing-bracket-spacing": ["error", {startTag: "never", endTag: "never", selfClosingTag: "never"}],
            "vue/no-multiple-template-root": "off",
            "vue/singleline-html-element-content-newline": "off",
            "vue/mustache-interpolation-spacing": ["error", "never"],
            "vue/operator-linebreak": ["error", "after"],
            "vue/no-mutating-props": ["error", {shallowOnly: true}],

            "@typescript-eslint/return-await": ["error", "always"],
            "@typescript-eslint/strict-boolean-expressions": "off",
            "@typescript-eslint/no-unused-vars": [
                "error",
                {
                    args: "all",
                    argsIgnorePattern: "^_",
                    caughtErrors: "all",
                    caughtErrorsIgnorePattern: "^_",
                    destructuredArrayIgnorePattern: "^_",
                    varsIgnorePattern: "^_",
                    ignoreRestSiblings: true
                }
            ],

            "@stylistic/space-before-function-paren": ["error", {named: "never", anonymous: "never", asyncArrow: "always"}],
            "@stylistic/max-len": ["error", {code: 140, ignoreComments: true}],
            "@stylistic/indent": ["error", 4],
            "@stylistic/indent-binary-ops": ["error", 4],
            "@stylistic/comma-dangle": ["error", "never"],
            "@stylistic/quotes": ["error", "double", {allowTemplateLiterals: true}],
            "@stylistic/object-curly-spacing": ["error", "never"],
            "@stylistic/brace-style": ["error", "1tbs", {allowSingleLine: true}],
            "@stylistic/block-spacing": ["error", "never"],
            "@stylistic/spaced-comment": ["error", "never"],
            "@stylistic/arrow-parens": ["error", "always"],
            "@stylistic/operator-linebreak": ["error", "after"],
            "@stylistic/comma-spacing": "error"
        }
    },
    {
        files: ["components/*/**"],
        rules: {
            "vue/multi-word-component-names": "off"
        }
    },
    {
        files: ["**/*.vue"],
        rules: {
            "@stylistic/indent": "off"
        }
    }
)
