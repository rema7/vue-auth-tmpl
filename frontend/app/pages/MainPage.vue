<template>
    <div
        class="row h-100"
    >
        <div class="col p-0">
            <h2>Logged In</h2>
            <button
                class="btn btn-sm align-middle btn-outline-secondary"
                @click="logout"
            >
                Logout
            </button>
        </div>
    </div>
</template>

<script>

import { AUTH_LOGOUT } from 'store/actions/Auth'

export default {
    name: 'MainPage',
    components: {
    },
    created () {
    },
    methods: {
        logout () {
            this.$store.dispatch('auth/' + AUTH_LOGOUT).then(() => {
                this.$router.push('/login')
            })
        },
    },
}
</script>
