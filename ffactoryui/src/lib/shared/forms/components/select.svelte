<script lang="ts">
    export type SelectKeyValue = {
        key: string,
        value: string,
    }

    const {options, ...rest}: { options: SelectKeyValue[] } = $props();
    let value = $state();
</script>

<select>
    {#each options as option}
        <p>{option}</p>
        <option value={option}>{option}</option>
    {/each}
</select>

<style>
    select {
        width: 100%;
        padding: .5em;
    }
</style>