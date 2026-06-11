import api from './api'
import { UserCreateInput, UserLoginInput, AuthResponse } from '@/types/auth'

export const authService = {
  register: async (data: UserCreateInput) => {
    const response = await api.post('/v1/auth/register', data)
    return response.data
  },

  login: async (data: UserLoginInput) => {
    const response = await api.post('/v1/auth/login', data)
    if (response.data.access_token) {
      localStorage.setItem('access_token', response.data.access_token)
      localStorage.setItem('refresh_token', response.data.refresh_token)
    }
    return response.data
  },

  logout: async () => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    return api.post('/v1/auth/logout')
  },

  refreshToken: async () => {
    const response = await api.post('/v1/auth/refresh-token')
    if (response.data.access_token) {
      localStorage.setItem('access_token', response.data.access_token)
    }
    return response.data
  },

  verifyOtp: async (email: string, otp: string) => {
    return api.post('/v1/auth/verify-otp', { email, otp })
  },
}
