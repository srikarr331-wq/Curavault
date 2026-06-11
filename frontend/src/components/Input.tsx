interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
}

export const Input = ({
  label,
  error,
  className = '',
  ...props
}: InputProps) => {
  return (
    <div className="flex flex-col gap-2">
      {label && <label className="label">{label}</label>}
      <input className={`input ${className}`} {...props} />
      {error && <span className="text-sm text-red-600">{error}</span>}
    </div>
  )
}
