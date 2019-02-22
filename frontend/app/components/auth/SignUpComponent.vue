<template>
    <div class="row justify-content-center h-100 align-items-center">
        <div class="col-lg-4 col-md-6 col-sm-8 col-xs-10">
            <form @submit.prevent="signUp">
                <div
                    class="form-group"
                    align="center"
                >
                    <h1>REMA</h1>
                </div>
                <div class="form-group">
                    <label for="inputEmail">Email</label>
                    <input
                        id="inputEmail"
                        v-model="email"
                        v-validate="'required|email'"
                        type="email"
                        name="email"
                        :class="{
                            'form-control': true,
                            'is-invalid': errors.has('email'),
                        }"
                        aria-describedby="emailHelp"
                        placeholder="Enter an email"
                    >
                    <span
                        v-show="errors.has('email')"
                        class="invalid-feedback"
                    >
                        {{ errors.first('email') }}
                    </span>
                </div>
                <div class="form-group">
                    <label for="inputPassword">Password</label>
                    <input
                        id="inputPassword"
                        ref="password"
                        v-model="password"
                        v-validate="'required'"
                        type="password"
                        :class="{
                            'form-control': true,
                            'is-invalid': errors.has('password'),
                        }"
                        placeholder="Enter password"
                        name="password"
                    >
                    <span
                        v-show="errors.has('password')"
                        class="invalid-feedback"
                    >
                        {{ errors.first('password') }}
                    </span>
                </div>
                <div class="form-group">
                    <label for="inputConfirmPassword">Confirm Password</label>
                    <input
                        id="inputConfirmPassword"
                        v-model="confirmPassword"
                        v-validate="'required|confirmed:password'"
                        :class="[
                            'form-control',
                            {'is-invalid': errors.has('confirmPassword')},
                        ]"
                        data-vv-as="password"
                        type="password"
                        placeholder="Enter password"
                        name="confirmPassword"
                    >
                    <span
                        v-show="errors.has('confirmPassword')"
                        class="invalid-feedback"
                    >
                        {{ errors.first('confirmPassword') }}
                    </span>
                </div>
                <button
                    class="btn btn-primary btn-block form-control"
                    type="submit"
                    @mousedown.prevent
                    :disabled="!isCompleted || errors.any()"
                >
                    Sign Up
                </button>
            </form>
            <router-link to="/login">
                <small>Back to login</small>
            </router-link>
        </div>
    </div>
</template>

<script>
import { AUTH_REGISTRATION_REQUEST } from 'store/actions/Auth'

export default {
    name: 'SignUpComponent',
    inject: ['$validator'],
    data () {
        return {
            email: '',
            password: '',
            confirmPassword: '',
        }
    },
    computed: {
        isCompleted () {
            return this.email && this.password && this.confirmPassword
        },
    },
    methods: {
        signUp () {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.$store.dispatch('auth/' + AUTH_REGISTRATION_REQUEST, {
                        email: this.email,
                        password: this.password,
                    }).then((result) => result && this.$router.push('/login'))
                }
            })
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
.form-control {
    margin-bottom: .5rem;
    font-size: .88rem;
}
</style>
