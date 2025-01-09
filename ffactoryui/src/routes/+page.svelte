<script lang="ts">
    import ModelSelector from "$lib/llm/components/model-selector.svelte";
    import {fetchModels} from "$lib/llm/api/fetch-models";
    import '@picocss/pico/css/pico.min.css'
    import Title from "$lib/shared/layout/components/title.svelte";
    import type {SelectKeyValue} from "$lib/shared/forms/components/select.svelte";
    import Chatbox from "$lib/llm/components/chatbox.svelte";

    let models: SelectKeyValue[] = $state([]);

    $effect(() => {
        fetchModels().then(data => {
            if (data && data.models.length > 0) {
                models = data.models.map((item) => ({
                    key: item,
                    value: item,
                }));
            }
        });
    })

    $inspect(models)
</script>

<section>
    <Title>FFactory</Title>

    <ModelSelector {models}/>
    <Chatbox></Chatbox>
</section>

<style>
</style>