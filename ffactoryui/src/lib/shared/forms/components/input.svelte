<script lang="ts">
    const {...rest} = $props();
    let value = $state();
</script>

<input class="input" bind:value {...rest}/>

<style>
</style>