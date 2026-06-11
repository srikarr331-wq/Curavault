import { Outlet, Link } from 'react-router-dom'

export const Layout = () => {
  return (
    <div className="flex h-screen flex-col">
      {/* Header */}
      <header className="border-b border-gray-200 bg-white shadow-sm">
        <nav className="container flex h-16 items-center justify-between">
          <Link to="/" className="text-xl font-bold text-blue-600">
            CuraVault
          </Link>
          <div className="flex items-center gap-4">
            <Link to="/dashboard" className="text-sm text-gray-600 hover:text-gray-900">
              Dashboard
            </Link>
            <Link to="/records" className="text-sm text-gray-600 hover:text-gray-900">
              Records
            </Link>
            <Link to="/profile" className="text-sm text-gray-600 hover:text-gray-900">
              Profile
            </Link>
            <Link to="/logout" className="text-sm text-red-600 hover:text-red-700">
              Logout
            </Link>
          </div>
        </nav>
      </header>

      {/* Main Content */}
      <main className="flex-1 overflow-auto bg-gray-50">
        <div className="container py-8">
          <Outlet />
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-200 bg-white py-6">
        <div className="container text-center text-sm text-gray-600">
          <p>&copy; 2024 CuraVault. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}
