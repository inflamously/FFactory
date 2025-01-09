<script lang="ts">
    import type {Snippet} from "svelte";

    const {children}: { children?: Snippet } = $props()
</script>

<div class="box">
    {@render children?.()}
</div>

<style>
    :root {
        --box-padding: 1em;
        --box-padding-bottom: 0;
        --box-margin-bottom: 1em;
        --box-border-color: var(--theme-color-secondary);
    }

    .box {
        background-color: var(--theme-color-secondary);
        border-radius: 4px;
        border: solid 3px var(--theme-color-quaternary);
        padding: var(--box-padding) var(--box-padding) var(--box-padding-bottom) var(--box-padding);
        margin-bottom: var(--box-margin-bottom);
    }
</style>