<script lang="ts">
    import Select, {type SelectKeyValue} from '$lib/shared/forms/components/select.svelte'
    import Box from '$lib/shared/layout/components/box.svelte'

    const {models}: { models: SelectKeyValue[] } = $props()
</script>

<Box>
    <Select options={models}/>
</Box>

<style>

</style>