<script lang="ts">
    import type {ChatMessageRole} from "$lib/llm/components/chatbox-message.svelte";

    type ChatMessage = {
        avatar: string;
        message: string;
        role: ChatMessageRole;
    }

    import Box from "$lib/shared/layout/components/box.svelte";
    import ChatboxMessage from "./chatbox-message.svelte";

    const {
        messages = [
            {
                avatar: "https://placehold.co/128x128",
                message: "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
                role: "user",
            },
            {
                avatar: "https://placehold.co/128x128",
                message: "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
                role: "user",
            }
        ]
    }: { messages: ChatMessage[] } = $props()
</script>

<Box --box-padding-bottom="1em">
    <div class="chat-window">
        {#each messages as message}
            <ChatboxMessage {...message}/>
        {/each}
    </div>
</Box>

<style>
    .chat-window {
        display: flex;
        flex-direction: column;
        row-gap: 1em;
        padding: 1em;
        max-height: 75vh;
        width: 100%;
        height: 100%;
        border-radius: .25em;
        background-color: var(--theme-color-content);
        overflow: hidden;
        overflow-y: scroll;
    }
</style>