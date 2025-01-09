<script lang="ts">
    const {src} = $props()
</script>

<div class="chat-message-icon">
    <img width="64" height="64" alt="role-icon" {src} />
</div>

<style>
    .chat-message-icon {
        display: inline-block;
        width: 4em;
        height: 4em;
        background: red;
        clip-path: polygon(30% 0, 100% 0, 100% 70%, 90% 90%, 70% 100%, 0 100%, 0 73%, 0 30%, 10% 10%);
    }

    img {
        position: relative;
        left: .15em;
        top: .15em;
        width: 3.7em;
        height: 3.7em;
        margin-bottom: .3em;
        clip-path: polygon(30% 0, 100% 0, 100% 70%, 90% 90%, 70% 100%, 0 100%, 0 73%, 0 30%, 10% 10%);
    }
</style>