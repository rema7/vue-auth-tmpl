import axios from 'axios'
import humps from 'humps'
import { getToken } from './storage'


const commonHeaders = Object.assign({}, {
    Accept: 'application/json',
})

const getWrapper = async (url, headers, params, cancelToken) => {
    return axios.get(url, {
        headers,
        params: humps.decamelizeKeys(params),
        cancelToken,
    }).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const get = async (url, params, cancelToken) => {
    return getWrapper(url, commonHeaders, params, cancelToken)
}

export const getSecured = async (url, params, cancelToken) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return getWrapper(url, headers, params, cancelToken)
}

const postWrapper = async (url, data, headers, cancelToken) => {
    return axios.post(
        url,
        humps.decamelizeKeys(data),
        {
            headers,
            cancelToken,
        }
    ).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const post = async (url, data, cancelToken) => {
    return postWrapper(url, data, commonHeaders, cancelToken)
}

export const postSecured = async (url, data, cancelToken) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return postWrapper(url, data, headers, cancelToken)
}

const deleteWrapper = async (url, headers) => {
    return axios.delete(
        url,
        { headers }
    ).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const deleteSecured = async (url) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return deleteWrapper(url, headers)
}

export const getCancelSource = () => {
    return axios.CancelToken.source()
}
