import { create } from 'zustand'
import { ReportResponse } from '@/types/report'

interface ReportStore {
  reports: ReportResponse[]
  selectedReport: ReportResponse | null
  isLoading: boolean
  setReports: (reports: ReportResponse[]) => void
  setSelectedReport: (report: ReportResponse | null) => void
  setLoading: (value: boolean) => void
  addReport: (report: ReportResponse) => void
  removeReport: (reportId: string) => void
}

export const useReportStore = create<ReportStore>((set) => ({
  reports: [],
  selectedReport: null,
  isLoading: false,
  setReports: (reports) => set({ reports }),
  setSelectedReport: (report) => set({ selectedReport: report }),
  setLoading: (value) => set({ isLoading: value }),
  addReport: (report) => set((state) => ({ reports: [...state.reports, report] })),
  removeReport: (reportId) =>
    set((state) => ({
      reports: state.reports.filter((r) => r.id !== reportId),
    })),
}))
