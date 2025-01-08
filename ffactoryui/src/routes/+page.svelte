<script lang="ts">
    import ModelSelector from "$lib/llm/components/model-selector.svelte";
    import {fetchModels} from "$lib/llm/api/fetch-models";

    let models = $state([]);

    $effect(() => {
        fetchModels().then(data => {
            if (data && data.models.length > 0) {
                models = data.models;
            }
        });
    })
</script>

<section>
    <h1>FFactory</h1>

    <ModelSelector {models}/>
</section>

<style>

</style>