import api from './api'
import { ReportCreateInput, ReportResponse } from '@/types/report'

export const reportService = {
  uploadReport: async (file: File, data: ReportCreateInput) => {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('title', data.title)
    formData.append('report_type', data.report_type)
    if (data.description) formData.append('description', data.description)
    if (data.test_date) formData.append('test_date', data.test_date)
    if (data.doctor_name) formData.append('doctor_name', data.doctor_name)

    return api.post('/v1/reports/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
  },

  listReports: async (skip: number = 0, limit: number = 10, reportType?: string) => {
    return api.get('/v1/reports', {
      params: { skip, limit, report_type: reportType },
    })
  },

  getReport: async (reportId: string) => {
    return api.get(`/v1/reports/${reportId}`)
  },

  updateReport: async (reportId: string, data: Partial<ReportCreateInput>) => {
    return api.put(`/v1/reports/${reportId}`, data)
  },

  deleteReport: async (reportId: string) => {
    return api.delete(`/v1/reports/${reportId}`)
  },

  downloadReport: async (reportId: string) => {
    return api.get(`/v1/reports/${reportId}/download`, {
      responseType: 'blob',
    })
  },

  searchReports: async (query: string, skip: number = 0, limit: number = 10) => {
    return api.get('/v1/reports/search', {
      params: { query, skip, limit },
    })
  },
}
