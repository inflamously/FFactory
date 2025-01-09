<script lang="ts">
    const {children} = $props()
</script>

<main class="container-fluid">
    {@render children?.()}
</main>

<style>
    :root {
        --theme-color-primary: rgb(22, 196, 127);
        --theme-color-secondary: rgb(255, 214, 90);
        --theme-color-tertiary: rgb(255, 157, 35);
        --theme-color-quaternary: rgb(249, 56, 39);

        --theme-color-content: rgb(255, 255, 255);

        background-color: var(--theme-color-tertiary);
        padding-top: 1em;
    }
</style>