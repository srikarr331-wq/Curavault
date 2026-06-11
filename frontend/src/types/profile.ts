// Patient Profile Types
export interface PatientProfile {
  id: string
  user_id: string
  dob?: string
  gender?: 'M' | 'F' | 'Other'
  blood_group?: string
  height?: number
  weight?: number
  allergies?: string[]
  chronic_conditions?: string[]
  emergency_contact_name?: string
  emergency_contact_phone?: string
  profile_image_url?: string
  created_at: string
  updated_at: string
}
