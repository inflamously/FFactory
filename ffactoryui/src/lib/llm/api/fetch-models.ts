import {error} from "@sveltejs/kit";

type LLMModelsDTO = {
    models: string[]
}

export const fetchModels = async (): Promise<LLMModelsDTO> | never => {
    const res = await fetch('http://localhost:8080/models', {
        method: 'GET'
    })

    if (!res.ok) {
        error(res.status, res.statusText)
    }

    return await res.json()
}