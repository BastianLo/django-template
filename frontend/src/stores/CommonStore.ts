import {defineStore} from 'pinia'
import {useAuthStore} from "@/stores/AuthStore";
import {useRouter} from "vue-router";

export default async function authorizedFetch(url: string, options: RequestInit = {}): Promise<Response> {
    useCommonStore().request_fetching = true;
    options.headers = {
        ...options.headers,
        Authorization: `Bearer ${await useAuthStore().get_valid_token()}`,
    };
    const fetch_response = fetch(url, options);
    fetch_response.then(() => {
        useCommonStore().request_fetching = false;
    })
    return fetch_response;
}

export const useCommonStore = defineStore({
    id: 'commonStore',
    state: () => ({
        request_fetching: false,
        router: useRouter(),
    }),
    getters: {},
    actions: {}
})