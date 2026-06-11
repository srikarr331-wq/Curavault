// Auth Types
export interface UserCreateInput {
  email: string
  full_name: string
  password: string
  confirm_password: string
  phone?: string
}

export interface UserLoginInput {
  email: string
  password: string
}

export interface AuthResponse {
  access_token: string
  refresh_token: string
  token_type: string
  expires_in: number
}

export interface User {
  id: string
  email: string
  full_name: string
  phone?: string
  role: 'patient' | 'doctor' | 'hospital_admin' | 'system_admin'
  is_active: boolean
  is_verified: boolean
  email_verified_at?: string
  last_login?: string
  created_at: string
  updated_at: string
}
