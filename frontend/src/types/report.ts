// Report Types
export interface ReportCreateInput {
  title: string
  description?: string
  report_type: string
  test_date?: string
  doctor_name?: string
  lab_name?: string
}

export interface ReportResponse {
  id: string
  user_id: string
  title: string
  description?: string
  report_type: string
  test_date?: string
  doctor_name?: string
  lab_name?: string
  file_url: string
  file_size: number
  mime_type: string
  extracted_text?: string
  ai_summary?: string
  created_at: string
  updated_at: string
}
