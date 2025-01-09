<script lang="ts">
    import ChatboxMessageIcon from './chatbox-message-icon.svelte'

    export type ChatMessageRole = 'user' | 'assistant' | 'system' | 'tool';

    const {role, avatar, message}: {
        role: ChatMessageRole,
        avatar: string,
        message: string
    } = $props();
    const roleFormatted = role[0].toUpperCase() + role.slice(1)
    const messagePlacement = role === 'user' ? 'end' : 'start'
</script>

<div class="chat-message" style:justify-content="{messagePlacement}">
    <div class="chat-message__content">
        <div class="chat-message__user-details">
            <span class="chat-message__role">{roleFormatted}</span>
            {#if avatar}
                <div class="chat-message__avatar">
                    <ChatboxMessageIcon src={avatar}/>
                </div>
            {/if}
        </div>
        {message}
    </div>
</div>

<style>
    .chat-message {
        display: flex;
    }

    .chat-message__user-details {
        display: flex;
        flex-direction: column;
        row-gap: .5em;
        padding-right: 1em;
    }

    .chat-message__content {
        display: flex;
        background-color: var(--theme-color-secondary);
        border-radius: .5em;
        padding: 0.5em 1em;
        font-size: .8em;
        flex-grow: 1;
        max-width: 40vw;
    }

    .chat-message__role {
        text-align: right;
        font-weight: 700;
        padding-right: .5em
    }

    .chat-message__avatar {
        display: inline-block;
        padding-right: .5em;
        flex-shrink: 1;
    }
</style>