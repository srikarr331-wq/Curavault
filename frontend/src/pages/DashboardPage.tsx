import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { reportService } from '@/services/reportService'
import { Button } from '@/components/Button'
import toast from 'react-hot-toast'

export const DashboardPage = () => {
  const [selectedType, setSelectedType] = useState<string | undefined>()

  const { data: reportsData, isLoading } = useQuery({
    queryKey: ['reports', selectedType],
    queryFn: () => reportService.listReports(0, 10, selectedType),
  })

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Health Dashboard</h1>
          <p className="mt-2 text-gray-600">Manage your medical records and health information</p>
        </div>
        <Button variant="primary" onClick={() => window.location.href = '/upload'}>
          Upload Report
        </Button>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
        <div className="card p-6">
          <h3 className="text-sm font-medium text-gray-600">Total Reports</h3>
          <p className="mt-2 text-3xl font-bold text-gray-900">
            {reportsData?.data?.length || 0}
          </p>
        </div>
        <div className="card p-6">
          <h3 className="text-sm font-medium text-gray-600">Last Updated</h3>
          <p className="mt-2 text-lg font-semibold text-gray-900">Today</p>
        </div>
        <div className="card p-6">
          <h3 className="text-sm font-medium text-gray-600">Blood Group</h3>
          <p className="mt-2 text-3xl font-bold text-gray-900">O+</p>
        </div>
      </div>

      {/* Recent Reports */}
      <div className="card p-6">
        <h2 className="mb-4 text-xl font-semibold text-gray-900">Recent Reports</h2>
        {isLoading ? (
          <p className="text-gray-600">Loading reports...</p>
        ) : reportsData?.data?.length ? (
          <div className="space-y-4">
            {reportsData.data.map((report: any) => (
              <div
                key={report.id}
                className="flex items-center justify-between border-b border-gray-200 pb-4 last:border-b-0"
              >
                <div>
                  <p className="font-medium text-gray-900">{report.title}</p>
                  <p className="text-sm text-gray-600">{report.test_date || 'N/A'}</p>
                </div>
                <Button variant="secondary" size="sm">
                  View
                </Button>
              </div>
            ))}
          </div>
        ) : (
          <p className="text-gray-600">No reports uploaded yet</p>
        )}
      </div>
    </div>
  )
}
