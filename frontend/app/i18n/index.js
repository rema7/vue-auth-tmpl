import Vue from 'vue'
import VueI18n from 'vue-i18n'

import en from './en'
import ru from './ru'

Vue.use(VueI18n)

const messages = {
    en,
    ru,
}

const selectedLocale = localStorage.getItem('locale') || navigator.language
console.log(selectedLocale)

const i18n = new VueI18n({
    locale: selectedLocale,
    fallbackLocale: 'en',
    messages,
})


export default i18n
