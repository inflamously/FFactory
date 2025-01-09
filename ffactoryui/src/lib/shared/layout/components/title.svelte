<script lang="ts">
    import {type Snippet} from 'svelte'

    const {type, children}: { type?: string, children: Snippet } = $props()
</script>

{#if type === 'h2'}
    <h2>{@render children?.()}</h2>
{:else if type === 'h3'}
    <h3>{@render children?.()}</h3>
{:else if type === 'h4'}
    <h4>{@render children?.()}</h4>
{:else if type === 'h5'}
    <h5>{@render children?.()}</h5>
{:else if type === 'h6'}
    <h6>{@render children?.()}</h6>
{:else}
    <h1>{@render children?.()}</h1>
{/if}

<style>
    :root {
        --title-color: var(--theme-color-secondary);
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--title-color)
    }
</style>
