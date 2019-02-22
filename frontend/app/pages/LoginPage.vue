<template>
    <div class="container h-100">
        <login-component />
    </div>
</template>

<script>
import LoginComponent from 'components/auth/LoginComponent'

export default {
    name: 'LoginPage',
    components: { LoginComponent },
}
</script>
