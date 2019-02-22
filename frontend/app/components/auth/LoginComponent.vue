<template>
    <div class="row justify-content-center h-100 align-items-center">
        <div class="col-lg-4 col-md-6 col-sm-8 col-xs-10">
            <form @submit.prevent="login">
                <div
                    class="form-group"
                    align="center"
                >
                    <h1 class="logo">BE MY WAYS</h1>
                </div>
                <div class="form-group">
                    <label for="inputEmail">Email</label>
                    <input
                        id="inputEmail"
                        v-model="email"
                        v-validate="'required|email'"
                        name="email"
                        type="email"
                        class="form-control"
                        aria-describedby="emailHelp"
                        placeholder="Enter an email"
                    >
                </div>
                <div class="form-group">
                    <label for="inputPassword">Password</label>
                    <input
                        id="inputPassword"
                        v-model="password"
                        v-validate="'required'"
                        name="password"
                        type="password"
                        class="form-control"
                        placeholder="Enter password"
                    >
                </div>
                <button
                    class="btn btn-primary btn-block form-control"
                    type="submit"
                    @mousedown.prevent
                    :disabled="!isCompleted || errors.any()"
                >
                    Login
                </button>
            </form>
            <router-link to="/signup">
                <small>Sign up</small>
            </router-link>
        </div>
    </div>
</template>

<script>
import { AUTH_REQUEST } from 'store/actions/Auth'
import { ACCOUNT_REQUEST } from 'store/actions/Account'

export default {
    name: 'LoginComponent',
    inject: ['$validator'],
    data () {
        return {
            email: '',
            password: '',
        }
    },
    computed: {
        isCompleted () {
            return this.email && this.password
        },
    },
    methods: {
        async login () {
            const result = await this.$store.dispatch('auth/' + AUTH_REQUEST, {
                email: this.email,
                password: this.password,
            })
            if (result) {
                await this.$store.dispatch('account/' + ACCOUNT_REQUEST)

                this.$router.push(this.$route.query.redirect || '/')
            }
        },
    },
}
</script>

<style scoped="scss">
label {
    margin-bottom: .75rem;
    font-size: .88rem;
    font-weight: 500;
}
.logo {
    color: #002364;
}
.form-control {
    margin-bottom: .5rem;
    font-size: .88rem;
}
</style>
