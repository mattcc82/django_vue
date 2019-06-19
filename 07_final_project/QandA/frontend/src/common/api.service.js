import { CSRF_TOKEN } from './csrf_token.js'
import axios from 'axios'

const apiService = axios.create({
  baseURL: '',
  timeout: 2000,
  headers: {
    'content-type': 'application/json',
    'X-CSRFTOKEN': CSRF_TOKEN
  }
})

export { apiService }
