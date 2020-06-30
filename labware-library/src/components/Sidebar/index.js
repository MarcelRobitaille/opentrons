// @flow
// main application sidebar
import * as React from 'react'
import type { FilterParams } from '../../types'
import { LabwareGuide } from './LabwareGuide'
import { FilterManufacturer } from './FilterManufacturer'
import { FilterCategory } from './FilterCategory'
import { FilterReset } from './FilterReset'
import styles from './styles.css'

export type SidebarProps = {|
  filters: FilterParams,
|}

export function Sidebar(props: SidebarProps): React.Node {
  const { filters } = props

  return (
    <nav className={styles.sidebar}>
      <LabwareGuide />
      <FilterManufacturer filters={filters} />
      <FilterCategory filters={filters} />
      <FilterReset filters={filters} />
    </nav>
  )
}
