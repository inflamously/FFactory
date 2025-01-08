<script lang="ts">
    const {children} = $props()
</script>

<div class="box">
    {@render children?.()}
</div>

<style>
    :root {
        --box-padding: 1em;
    }

    .box {
        border: 2px #ccc solid;
        padding: var(--box-padding);
    }
</style>